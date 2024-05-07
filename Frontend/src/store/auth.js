import { create } from 'zustand';
import { mountStoreDevtool } from 'simple-zustand-devtools';
import Cookies from 'js-cookie';
import jwt_decode from 'jwt-decode';

const UseAuthStore = create((set, get) => ({
  allUserData: null,
  loading: false,

  user: () => ({
    user_id: get().allUserData?.user_id || null,
    username: get().allUserData?.username || null,
  }),

  setUser: (user) => set({ allUserData: user }),
  setLoading: (isLoading) => set({ loading: isLoading }), // Correctly update loading state
  isLoggedIn: () => get().allUserData !== null,
}));

// Conditionally mount the store devtool based on the environment
if (process.env.NODE_ENV === 'development') {
  mountStoreDevtool('Store', UseAuthStore);
}

export { UseAuthStore };
