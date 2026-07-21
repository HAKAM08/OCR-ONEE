import { useQuery } from "@tanstack/react-query";
import { ViewerAPI } from "@/api/viewer";

export function useViewer(id: number) {
    return useQuery({
        queryKey: ["viewer", id],
        queryFn: () => ViewerAPI.getDocument(id),
        enabled: !!id,
    });
}