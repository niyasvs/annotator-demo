import Axios from "axios";
import { BASE_URL } from "./constants";

export async function login(email: string, password: string) {
  const response = await Axios.post(
    `${BASE_URL}auth/login`,
    {
      email,
      password,
    },
    { withCredentials: true }
  );

  return response;
}

export async function register(name: string, email: string, password: string) {
  return await Axios.post(`${BASE_URL}auth/register`, {
    name,
    email,
    password,
  });
}
