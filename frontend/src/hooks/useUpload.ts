import {
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";

import {
  UploadAPI,
  UploadRequest,
} from "@/api/upload";

export function useUpload() {

  const queryClient = useQueryClient();

  return useMutation({

    mutationFn: (data: UploadRequest) =>
      UploadAPI.upload(data),

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