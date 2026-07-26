import api from "@/api/axios";

export interface DashboardStats {

    total_documents: number;

    ocr_completed: number;

    processing: number;

    indexed: number;

    average_confidence: number;

detected_languages: {
    language: string;
    count: number;
}[];

    recent_documents: RecentDocument[];
}

export interface RecentDocument {

    id: number;

    filename: string;

    status: string;

    upload_date: string;
}

export const DashboardAPI = {

    async getStats(): Promise<DashboardStats> {

        const response = await api.get<DashboardStats>(
            "/dashboard/stats"
        );

        return response.data;

    }

};