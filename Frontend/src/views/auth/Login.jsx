// import React, {useState, useEffect} from 'react'
// import { login } from '../../utils/auth'
// import { useNavigate, Link } from 'react-router-dom'
// import { UseAuthStore } from '../../store/auth'

// function Login() {
//     const [email ,setEmail] = useState("")
//     const [password, setPassword] = useState("")
//     const [isLoading, setIsLoading] = useState(false)
//     const navigate = useNavigate()
//     const isLoggedIn = UseAuthStore((state) => state.isLoggedIn)

//     useEffect(() =>{
//         if (isLoggedIn()){
//             navigate('/')
//         }
//     })

//     const resetForm = () => {
//         setEmail("")
//         setPassword("")
//     }


//     const handleLogin = (e) => {
//         e.preventDefualt()
//         setIsLoading(true)

//         const {error} = login(email, password)
//         if (error){
//             alert(error)
//         } else {
//             navigate("/")
//             resetForm()
//         }
//         setIsLoading(false)
//     }


//   return (
//     <div>
//         <h2>Welcome Back</h2>
//         <p>Login To Continue</p>
//         <form onSubmit={handleLogin}>
//             <input
//                 type='"text'
//                 name= "email"
//                 id="email"
//                 value={email}
//                 onChange={(e) => setEmail(e.target.value)}
//             />
//             <br/>
//             <br/>
//             <input
//                 type='"password'
//                 name= "password"
//                 id="password"
//                 value={password}
//                 onChange={(e) => setPassword(e.target.value)}
//             />
//             <br/>
//             <br/>
//             <button type='submit'>Login</button>
               
//         </form>
//     </div>
//   )
// }

// export default Login


import React, { useState, useEffect } from 'react';
import { login } from '../../utils/auth';
import { useNavigate } from 'react-router-dom';
import { UseAuthStore } from '../../store/auth';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const isLoggedIn = UseAuthStore((state) => state.isLoggedIn);

  useEffect(() => {
    if (isLoggedIn()) {
      navigate('/');
    }
  }, [isLoggedIn, navigate]);

  const resetForm = () => {
    setEmail('');
    setPassword('');
  };

  const handleLogin = async (e) => {
    e.preventDefault(); // Corrected typo: preventDefault()

    setIsLoading(true);

    const { error } = await login(email, password); // Await login function

    if (error) {
      alert(error);
    } else {
      navigate('/');
      resetForm();
    }

    setIsLoading(false);
  };

  return (
    <div>
      <h2>Welcome Back</h2>
      <p>Login To Continue</p>
      <form onSubmit={handleLogin}>
        <input
          type="text" // Corrected type attribute
          name="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <br />
        <br />
        <input
          type="password" // Corrected type attribute
          name="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <br />
        <br />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
