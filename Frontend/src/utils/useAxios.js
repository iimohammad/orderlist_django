import axios from "axios";
import { isAccessTokenExpired,setAuthUser, getRefreshToken } from "./auth";
import { BASE_URL } from "./constants";
import Cookies from "js-cookie"

const useAxios = async () => {
    const access_toekn = Cookies.get(access_toekn)
    const refresh_toekn = Cookies.get(refresh_toekn)

    const axiosInstance = axios.create({
        baseURL: BASE_URL,
        headers: {Authorization: `Bearer ${access_toekn}`}
    })

    axiosInstance.interceptors.request.use(async(req)=>{
        if (!isAccessTokenExpired(access_toekn)){
            return req
        }

        const response = await getRefreshToken(refresh_toekn)
        setAuthUser(response.access, response.refresh)

        req.headers.Authorization = `Bearer ${response.data.access}`
        return req
    })
    return axiosInstance
}

export default useAxios