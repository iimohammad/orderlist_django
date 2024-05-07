import {Navigate} from 'react-router-dom'
import { UseAuthStore } from '../store/auth'

const PrivateRoute = ({children}) => {
    const loggedIn = UseAuthStore((state)=> state.isLoggedIn)()
    return loggedIn ? <>{children}</> : <Navigate to={'/login'} />
}

export default PrivateRoute