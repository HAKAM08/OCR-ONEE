import {

    useMutation,

    useQueryClient,

} from "@tanstack/react-query";

import { DocumentsAPI } from "@/api/documents";

export function useDeleteDocument() {

    const queryClient = useQueryClient();

    return useMutation({

        mutationFn: DocumentsAPI.delete,

        onSuccess: () => {

            queryClient.invalidateQueries({

                queryKey: ["documents"]

            });

        }

    });

}