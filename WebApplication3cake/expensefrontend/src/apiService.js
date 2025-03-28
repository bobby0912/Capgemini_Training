import axios from 'axios';

const API_URL = 'https://localhost:7156/api/expense'; // Adjust the URL as needed

export const getExpenses = async () => {
    const response = await axios.get(API_URL);
    return response.data;
};

export const addExpense = async (expense) => {
    const response = await axios.post(API_URL, expense);
    return response.data;
};

export const deleteExpense = async (id) => {
    await axios.delete(`${API_URL}/${id}`);
};
