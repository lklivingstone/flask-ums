from flask import jsonify, request, abort, Blueprint
from datetime import date, datetime
from flask_jwt_extended import jwt_required

from src.db import get_db

task_blueprint= Blueprint("task", __name__, url_prefix="/api")

@task_blueprint.route("/task", methods=['POST'])
@jwt_required()
def create_task():
    if request.method=="POST":
        db = get_db()
        cursor = db.cursor()

        statusList=["Incomplete", "In Progress", "Completed"]

        task_data = request.get_json()

        # Extract task properties from the request data
        title = task_data.get('title', '')
        description = task_data.get('description', '')
        due_date_str = task_data.get('due_date', '')
        status = task_data.get('status', '')

        if not due_date_str:
            return jsonify({"error": "Due date is required"}), 400
        
        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Invalid due date format. It should be 'YYYY-MM-DD'"}), 400
        
        year= int(due_date_str.split("-")[0])
        month= int(due_date_str.split("-")[1])
        dt= int(due_date_str.split("-")[2])

        due_date_value= (1000000*year) + (10000*month) + (100*dt)
         
        today_str = str(date.today())
        today_year= int(today_str.split("-")[0])
        today_month= int(today_str.split("-")[1])
        today_dt= int(today_str.split("-")[2])

        today_date_value= (1000000*today_year) + (10000*today_month) + (100*today_dt)

        if due_date_value < today_date_value:
            return jsonify({"error": "Due date should be today or later"}), 400

        if not status or status not in statusList:
            return jsonify({"error": "Status can only be  'Incomplete', 'In Progress', or 'Completed'"}), 400

        
        cursor.execute(
            'INSERT INTO task (title, description, due_date, status) VALUES (?, ?, ?, ?)',
            (title, description, due_date, status)
        )

        db.commit()

        return jsonify({"message": "Task created successfully"}), 201

@task_blueprint.route("/tasks", methods=['GET'])
@jwt_required()
def get_all_tasks():
    if request.method=="GET":
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        if page < 1:
            return jsonify({"error": "Invalid page number"}), 400
        
        db = get_db()
        cursor = db.cursor()

        cursor.execute('SELECT COUNT(*) FROM task')
        total_count = cursor.fetchone()[0]

        total_pages = (total_count // per_page) + (1 if total_count % per_page > 0 else 0)

        offset = (page - 1) * per_page

        cursor.execute('SELECT * FROM task LIMIT ? OFFSET ?', (per_page, offset))
        rows = cursor.fetchall()

        tasks = []
        for row in rows:
            task = {
                'id': row[0],
                'title': row[1],
                'description': row[2],
                'due_date': row[4],
                'status': row[3]
            }
            tasks.append(task)

        if len(tasks)==0:
            return jsonify({"error": "Invalid Page Number"}), 400

        return jsonify({"data": tasks,
                        'page': page,
                        'per_page': per_page,
                        'total_pages': total_pages,
                        'total_count': total_count}), 201


@task_blueprint.route("/task/<int:id>", methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def task(id=0):
    if request.method=="GET":
        db = get_db()
        cursor = db.cursor()
        
        cursor.execute(
            'SELECT * FROM task WHERE id = ?', (id,)
        )

        row = cursor.fetchone()

        if row is None:
            return jsonify({
                'error': f"Task with ID={id} not found in the database."
            }), 404

        found_task = {
            'id': row[0],
            'title': row[1],
            'description': row[2],
            'due_date': row[4],
            'status': row[3]
        }
        return jsonify({
            'data': found_task
        }), 200
    
    if request.method=="PUT":
        db = get_db()
        cursor = db.cursor()
        
        cursor.execute('SELECT * FROM task WHERE id = ?', (id,))

        row = cursor.fetchone()

        if row is None:
            return jsonify({
                'error': f"Task with ID={id} not found in the database."
            }), 404

        status = request.json.get('status', row[4])
        title = request.json.get('title', row[1])
        description = request.json.get('description', row[2])
        due_date = request.json.get('due_date', row[3])

        cursor.execute(
            'UPDATE task SET status = ?, title = ?, description = ?, due_date = ? WHERE id = ?',
            (status, title, description, due_date, id)
        )

        db.commit()

        updated_task = {
            'id': id,
            'title': title,
            'description': description,
            'due_date': due_date,
            'status': status
        }


        return jsonify({
            'data': updated_task
        }), 200
    
    if request.method=="DELETE":
        db = get_db()
        cursor = db.cursor()
        
        cursor.execute(
            'SELECT * FROM task WHERE id = ?', (id,)
        )

        row = cursor.fetchone()

        if row is None:
            return jsonify({
                'error': f"Task with ID={id} not found in the database."
            }), 404

        cursor.execute('DELETE FROM task WHERE id = ?', (id,))
        db.commit()

        return jsonify({
            "message": "Task deleted successfully"
        }), 200


