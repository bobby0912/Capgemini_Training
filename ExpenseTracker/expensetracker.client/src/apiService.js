import axios from 'axios';

const API_URL = 'https://localhost:7179/api/Expense'; // Adjust the URL as needed

export const getExpenses = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        if (error.code === 'ERR_NETWORK') {
            console.error('Network error: Please check your connection.');
        } else {
            console.error('An error occurred:', error.message);
        }
        throw error; // Re-throw the error if you want to handle it further up the call stack
    }
};

export const addExpense = async (expense) => {
    const response = await axios.post(API_URL, expense);
    return response.data;
};

export const deleteExpense = async (id) => {
    await axios.delete(`${API_URL}/${id}`);
};
