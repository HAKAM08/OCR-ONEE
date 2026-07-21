import api from "@/api/axios";

export interface ViewerDocument {

    id: number;

    original_filename: string;

    filename: string;

    file_type: string;

    file_path: string;

    status: string;

    upload_date: string;

    language: string;

    confidence: number;

    processing_time: number;

    text: string;

}

export const ViewerAPI = {

    async getDocument(id: number): Promise<ViewerDocument> {

        const response = await api.get<ViewerDocument>(
            `/viewer/${id}`
        );

        return response.data;

    }

};