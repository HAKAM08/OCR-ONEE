import {
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";

import { UploadAPI } from "@/api/upload";

export function useUpload() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: UploadAPI.upload,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["documents"],
      });

      queryClient.invalidateQueries({
        queryKey: ["dashboard"],
      });
    },
  });
}