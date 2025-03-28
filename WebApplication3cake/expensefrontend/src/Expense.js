import React, { useState, useEffect } from 'react';
import { getExpenses, addExpense, deleteExpense } from './apiService';
import './Expense.css';

const Expenses = () => {
    const [expenses, setExpenses] = useState([]);
    const [newExpense, setNewExpense] = useState({ description: '', amount: '', category: '' });
    const [expenseIdToDelete, setExpenseIdToDelete] = useState('');

    const fetchExpenses = async () => {
        const data = await getExpenses();
        setExpenses(data);
    };

    const handleAddExpense = async () => {
        await addExpense(newExpense);
        fetchExpenses();
        setNewExpense({ description: '', amount: '', category: '' });
    };

    const handleDeleteExpense = async () => {
        await deleteExpense(expenseIdToDelete);
        fetchExpenses();
        setExpenseIdToDelete('');
    };

    return (
        <div className="expenses-container">
            <h1>Expenses</h1>
            <button onClick={fetchExpenses} className="show-expenses-button">Show All Expenses</button>
            <ul>
                {expenses.map(expense => (
                    <li key={expense.id}>
                        ID: {expense.id} - {expense.description} - ${expense.amount} - {expense.category}
                    </li>
                ))}
            </ul>


            <div className="add-expense">
                <h2>Add Expense</h2>
                <input
                    type="text"
                    placeholder="Description"
                    value={newExpense.description}
                    onChange={(e) => setNewExpense({ ...newExpense, description: e.target.value })}
                />
                <input
                    type="number"
                    placeholder="Amount"
                    value={newExpense.amount}
                    onChange={(e) => setNewExpense({ ...newExpense, amount: e.target.value })}
                />
                <input
                    type="text"
                    placeholder="Category"
                    value={newExpense.category}
                    onChange={(e) => setNewExpense({ ...newExpense, category: e.target.value })}
                />
                <button onClick={handleAddExpense} className="add-expense-button">Add</button>
            </div>


            <div className="delete-expense">
                <h2>Delete Expense</h2>
                <input
                    type="text"
                    placeholder="Expense ID"
                    value={expenseIdToDelete}
                    onChange={(e) => setExpenseIdToDelete(e.target.value)}
                />
                <button onClick={handleDeleteExpense} className="delete-expense-button">Delete</button>
            </div>
        </div>
    );
};

export default Expenses;
