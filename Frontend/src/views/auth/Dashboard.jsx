import React from 'react';
import { Link } from 'react-router-dom';
import { UseAuthStore } from '../../store/auth';


const Dashboard = () => {
    const [isLoggedIn,setIsLoggedIn] = UseAuthStore((state) =>[
        state.isLoggedIn,
        state.user
    ])
    return (
        <>
            {isLoggedIn()
                ? <div> 
                    <h1>Dashboard</h1>
                    <Link to={`/logout`}>Logout</Link>
                </div> 
                : <div className="d-grid gap-3">
                <Link className="btn btn-primary btn-lg" to="/register">Register</Link>
                <Link className="btn btn-outline-primary btn-lg" to="/login">Login</Link>
                </div>
            }
        </>
    );
}

export default Dashboard;
