import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export interface Model {
  id: string;
  name: string;
  description: string;
}

export const api = {
  getModels: async (): Promise<Model[]> => {
    const response = await axios.get(`${API_BASE_URL}/models`);
    if (Array.isArray(response.data)) return response.data;
    if (Array.isArray(response.data.models)) return response.data.models;
    return [];
  },

  uploadVideo: async (file: File): Promise<{ filename: string }> => {
    const formData = new FormData();
    formData.append('file', file);
    const response = await axios.post(`${API_BASE_URL}/upload`, formData);
    return response.data;
  },

  processVideo: async (filename: string, model: string): Promise<void> => {
    await axios.post(`${API_BASE_URL}/process`, { filename, model });
  },

  getResultUrl: (filename: string): string => {
    return `${API_BASE_URL}/results/${filename}`;
  }
}; 