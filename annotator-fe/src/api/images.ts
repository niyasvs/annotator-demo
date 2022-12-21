import { BASE_URL } from "./constants";
import axios from "axios";

export async function listImages(projectId: string) {
  return await axios({
    url: `${BASE_URL}images/${projectId}`,
    method: "GET",
    withCredentials: true,
  });
}

export async function getImage(imageId: string) {
  return await axios({
    url: `${BASE_URL}images/find_one/${imageId}`,
    method: "GET",
    withCredentials: true,
  });
}

export async function postImages(projectId: string, files: any) {
  return await axios({
    url: `${BASE_URL}images/${projectId}`,
    method: "POST",
    data: files,
    withCredentials: true,
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
}

export async function saveAnnotation(imageId: string, annotations: any[]) {
  return await axios({
    url: `${BASE_URL}images/${imageId}`,
    method: "PUT",
    data: {
      annotations,
    },
    withCredentials: true,
  });
}
