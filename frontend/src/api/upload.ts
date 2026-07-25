import api from "@/api/axios";

export interface UploadResponse {
  id: number;
  original_filename: string;
  filename: string;
  file_type: string;
  file_path: string;
  upload_date: string;
  status: string;
  owner_id: number;
  document_type: string;
}

export interface UploadRequest {
  file: File;
  documentType: string;
}

export const UploadAPI = {
  async upload({
    file,
    documentType,
  }: UploadRequest): Promise<UploadResponse> {

    const formData = new FormData();

    formData.append("file", file);
    formData.append("document_type", documentType);

    const response = await api.post<UploadResponse>(
      "/documents/upload",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

    return response.data;
  },
};