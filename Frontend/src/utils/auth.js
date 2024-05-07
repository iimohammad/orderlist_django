import { UseAuthStore } from '../store/auth.js';
import axios from 'axios';
import jwt_decode from 'jwt-decode'
import Cookies from  'js-cookie'
import { BASE_URL } from './constants.js';
import apiInstance from './axios.js';

// export const login = async(email, password) => {
//     try {
//         const {data, status} = await axios.post(`${BASE_URL}user/token/`,{
//             email: email,
//             password: password,
//         })

//         if (status==200){
//             setAuthUser(data.access, data.refresh)
//             // Alert sign in successfully
//         }
//         return {data, error:null}
//     } catch(error){
//         return {
//             data: null,
//             error: error.response.data?.detail || "Something went wrong"
//         }
//     }
// }


export const login = async (email, password) => {
    try {
      const response = await apiInstance.post('user/token/', {
        email: email,
        password: password,
      });
  
      if (response.status === 200) {
        const { data } = response;
        setAuthUser(data.access, data.refresh);
        console.log('Login successful:', data);
      }
  
      return { data: response.data, error: null };
    } catch (error) {
      console.error('Login failed:', error.response.data);
      return {
        data: null,
        error: error.response.data?.detail || 'Something went wrong',
      };
    }
  };

export const register = async (full_name, email, phone, password, password2) => {
    try {
        const response = await axios.post(`${BASE_URL}user/register/`, {
            full_name: full_name,
            email: email,
            phone: phone,
            password: password,
            password2: password2,
      });
        // console.log('Registration successful:', response.data);

        // Handle response here (e.g., log user in automatically after registration)
        if (response.status === 201) {
            await login(email, password);
        }

        return { data: response.data, error: null };
    } catch (error) {
        return {
            data: null,
            error: error.response?.data?.detail || 'Something wentssssssssss wrong',
        };
    }
};

export const logout = () => {
    Cookies.remove("access_token")
    Cookies.remove("refresh_token")
    UseAuthStore.getState().setUser(null)

    // Alert - Signed out successfully
}

export const setUser = async () => {
    const accessToken = Cookies.get("access_toekn");
    const refreshToken = Cookies.get("refresh_toekn");

    if (!accessToken || ! refreshToken){
        return;
    }

    if (accessTokenExpired(accessToken)){
        const response = await getRefreshToken(refreshToken)
        setAuthUser(response.access, response.refresh)
    }else{
        setAuthUser(accessToken, refreshToken)
    }
}




export const setAuthUser = (accessToken, refreshToken) => {
    try {
      // Set access token and refresh token in cookies
      Cookies.set('access_token', accessToken, { expires: 1, secure: true });
      Cookies.set('refreshToken', refreshToken, { expires: 7, secure: true });
  
      // Decode the access token to get user information
      const user = jwt_decode(accessToken) ?? null;
  
      // Update the user and loading state in UseAuthStore if user data is available
      if (user) {
        UseAuthStore.getState().setUser(user); // Set user data in the store
      }
  
      // Set loading state to false in UseAuthStore
      UseAuthStore.getState().setLoading(false);
    } catch (error) {
      console.error('Error setting auth user:', error);
    }
  };








export const getRefreshToken = async () => {
    const refresh_toekn = Cookies.get("refresh_toekn")
    const response = await axios.post('user/token/refresh/',{
        refresh : refresh_toekn
    })
    return response.data
}

export const isAccessTokenExpired = (accessToken) => {
    try {
        const decodeToken = jwt_decode(accessToken)
        return decodeToken.exp < Date.now() /100
    } catch (error) {
        return true
    }
}





  
//   // Example usage
  const userFullName = 'Jo1233546 Doe';
  const userEmail = 'mamad1233456@example.com';
  const userPhone = '12711123386490';
  const userPassword = 'secretpassword';
  const userPasswordConfirmation = 'secretpassword';
  
register(userFullName, userEmail, userPhone, userPassword, userPasswordConfirmation);
  

// login(userEmail,userPassword)