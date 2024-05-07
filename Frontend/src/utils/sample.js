import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api/v1/';

// Example registration function
const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${BASE_URL}user/register/`, userData);
    console.log('Registration successful:', response.data);
    return response.data; // Handle response data as needed
  } catch (error) {
    console.error('Registration failed:', error.response.data);
    throw error; // Handle error appropriately in your frontend
  }
};

// Example usage
const userData = {
  full_name: 'John Doe',
  email: 'johndoe@example.com',
  phone: '1234567890',
  password: 'secretpassword',
  password2: 'secretpassword',
};

registerUser(userData);
