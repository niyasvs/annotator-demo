import { BASE_URL } from "./constants";
import axios from "axios";

export async function listProjects() {
  return await axios({
    url: `${BASE_URL}projects/`,
    method: "GET",
    withCredentials: true,
  });
}

export async function createProject(name: string) {
  return await axios({
    url: `${BASE_URL}projects/`,
    method: "POST",
    data: { name },
    withCredentials: true,
  });
}
