import { useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

import UploadDropzone from "@/components/upload/UploadDropzone";
import ProcessingProgress from "@/components/upload/ProcessingProgress";
import { useUpload } from "@/hooks/useUpload";
import { DocumentsAPI } from "@/api/documents";




export default function Upload() {
  const navigate = useNavigate();

  const upload = useUpload();
  const [progress, setProgress] = useState(0);

const [status, setStatus] = useState("");

  async function waitUntilCompleted(documentId: number) {

    const interval = setInterval(async () => {

        try {

            const document = await DocumentsAPI.getStatus(documentId);

            setStatus(document.status);

            switch (document.status) {

                case "UPLOADED":

                    setProgress(15);

                    break;

                case "PROCESSING":

                    setProgress(60);

                    break;

                case "INDEXING":

                    setProgress(90);

                    break;

                case "OCR_COMPLETED":

                    setProgress(100);

                    clearInterval(interval);

                    toast.success("OCR completed");

                    setTimeout(() => {

                        navigate(`/viewer/${documentId}`);

                    }, 800);

                    break;

            }

        }

        catch {

            clearInterval(interval);

        }

    },1000);

}

  async function handleUpload(file: File) {
    try {
const document = await upload.mutateAsync(file);

const documentId = document.id;
      toast.success("Document uploaded successfully.");

      waitUntilCompleted(documentId);
    } catch (error: any) {
      console.error(error);

      toast.error(
        error.response?.data?.detail ??
          "Upload failed."
      );
    }
  }

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold">
          Upload Document
        </h1>

        <p className="text-slate-500 mt-2">
          Upload a PDF or image. The system will automatically
          process it using OCR and open the viewer when the
          extraction is complete.
        </p>
      </div>

      <UploadDropzone onFile={handleUpload} />
      {progress > 0 && (

    <ProcessingProgress

        progress={progress}

        status={status}

    />

)}
    </div>
  );
}