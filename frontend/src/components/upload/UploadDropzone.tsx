import { useDropzone } from "react-dropzone";

interface Props {
  onFile: (file: File) => void;
}

export default function UploadDropzone({ onFile }: Props) {
  const {
    getRootProps,
    getInputProps,
    isDragActive,
  } = useDropzone({
    multiple: false,

    onDrop: (acceptedFiles) => {
      if (acceptedFiles.length > 0) {
        onFile(acceptedFiles[0]);
      }
    },
  });

  return (
    <div
      {...getRootProps()}
      className={`cursor-pointer rounded-xl border-2 border-dashed p-16 text-center transition ${
        isDragActive
          ? "border-blue-500 bg-blue-50"
          : "border-slate-300 bg-white"
      }`}
    >
      <input {...getInputProps()} />

      <h2 className="text-2xl font-bold">
        Drag & Drop your document
      </h2>

      <p className="mt-4 text-slate-500">
        or click here to browse
      </p>
    </div>
  );
}