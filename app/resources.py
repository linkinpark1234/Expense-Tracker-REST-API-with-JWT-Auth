from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Expense
from datetime import datetime
from sqlalchemy import func

expense_bp = Blueprint("expenses", __name__)


@expense_bp.route("/expenses", methods=["POST"])
@jwt_required()
def add_expense():
    user_id = get_jwt_identity()
    data = request.get_json()

    expense = Expense(
        title=data["title"],
        amount=data["amount"],
        category=data["category"],
        user_id=user_id
    )
    db.session.add(expense)
    db.session.commit()
    return jsonify({"message": "Expense added"}), 201


@expense_bp.route("/expenses", methods=["GET"])
@jwt_required()
def get_expenses():
    user_id = get_jwt_identity()
    category = request.args.get("category")

    query = Expense.query.filter_by(user_id=user_id)
    if category:
        query = query.filter_by(category=category)

    expenses = query.all()
    result = [
        {
            "id": e.id,
            "title": e.title,
            "amount": e.amount,
            "category": e.category,
            "date": e.date.strftime("%Y-%m-%d")
        }
        for e in expenses
    ]
    return jsonify(result), 200


@expense_bp.route("/expenses/<int:expense_id>", methods=["DELETE"])
@jwt_required()
def delete_expense(expense_id):
    user_id = get_jwt_identity()
    expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()

    if not expense:
        return jsonify({"message": "Expense not found"}), 404

    db.session.delete(expense)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"}), 200


@expense_bp.route("/expenses/summary", methods=["GET"])
@jwt_required()
def summary():
    user_id = get_jwt_identity()

    results = db.session.query(
        Expense.category,
        func.sum(Expense.amount).label("total")
    ).filter_by(user_id=user_id).group_by(Expense.category).all()

    summary_data = {row.category: row.total for row in results}
    return jsonify(summary_data), 200