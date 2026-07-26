import api from "@/api/axios";

export interface Document {
  id: number;
  original_filename: string;
  filename: string;
  file_type: string;
  upload_date: string;
  status: string;
  owner_id: number;
}

export interface DocumentStatus {
  id: number;
  status: string;
}

export const DocumentsAPI = {
  async getAll(): Promise<Document[]> {
    const response = await api.get<Document[]>("/documents");
    return response.data;
  },

  async getById(id: number): Promise<Document> {
    const response = await api.get<Document>(`/documents/${id}`);
    return response.data;
  },

  async getStatus(id: number): Promise<DocumentStatus> {
    const response = await api.get<DocumentStatus>(
      `/documents/${id}/status`
    );

    return response.data;
  },

  async delete(id: number): Promise<void> {
    await api.delete(`/documents/${id}`);
  },
};