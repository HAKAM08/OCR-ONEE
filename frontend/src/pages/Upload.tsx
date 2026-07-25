import { useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

import UploadDropzone from "@/components/upload/UploadDropzone";
import ProcessingProgress from "@/components/upload/ProcessingProgress";

import { useUpload } from "@/hooks/useUpload";
import { DocumentsAPI } from "@/api/documents";
import { useAuth } from "@/contexts/AuthContext";

export default function Upload() {

  const navigate = useNavigate();

  const upload = useUpload();

  const { user } = useAuth();

  const isAdmin = user?.role === "ADMIN";

  const [progress, setProgress] = useState(0);

  const [status, setStatus] = useState("");

  const [documentType, setDocumentType] =
    useState("COMMON");

  async function waitUntilCompleted(
    documentId: number
  ) {

    const interval = setInterval(async () => {

      try {

        const document =
          await DocumentsAPI.getStatus(
            documentId
          );

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

            toast.success(
              "OCR completed."
            );

            setTimeout(() => {

              navigate(
                `/viewer/${documentId}`
              );

            }, 800);

            break;

        }

      }

      catch {

        clearInterval(interval);

      }

    }, 1000);

  }

  async function handleUpload(
    file: File
  ) {

    try {

      const document =
        await upload.mutateAsync({

          file,

          documentType: isAdmin
            ? documentType
            : "COMMON",

        });

      toast.success(
        "Document uploaded successfully."
      );

      waitUntilCompleted(
        document.id
      );

    }

    catch (error: any) {

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

        <p className="mt-2 text-slate-500">

          Upload a PDF or image. The system will process
          the document using OCR.

        </p>

      </div>

      {isAdmin && (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

          <h2 className="mb-4 text-lg font-semibold">

            Document Type

          </h2>

          <div className="flex gap-8">

            <label className="flex cursor-pointer items-center gap-2">

              <input
                type="radio"
                value="COMMON"
                checked={documentType === "COMMON"}
                onChange={(e) =>
                  setDocumentType(
                    e.target.value
                  )
                }
              />

              <span>Common</span>

            </label>

            <label className="flex cursor-pointer items-center gap-2">

              <input
                type="radio"
                value="CONFIDENTIAL"
                checked={
                  documentType === "CONFIDENTIAL"
                }
                onChange={(e) =>
                  setDocumentType(
                    e.target.value
                  )
                }
              />

              <span>Confidential</span>

            </label>

          </div>

        </div>

      )}

      <UploadDropzone
        onFile={handleUpload}
      />

      {progress > 0 && (

        <ProcessingProgress
          progress={progress}
          status={status}
        />

      )}

    </div>

  );

}