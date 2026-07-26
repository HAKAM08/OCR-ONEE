import api from "@/api/axios";

export interface SearchResult {

    id: number;

    filename: string;

    original_filename: string;

    language: string;

    confidence: number;

    status: string;

    snippet: string;

}

export const SearchAPI = {

    async search(query: string): Promise<SearchResult[]> {

        const response = await api.get<SearchResult[]>(

            "/search",

            {

                params: {

                    q: query,

                },

            }

        );

        return response.data;

    },

};