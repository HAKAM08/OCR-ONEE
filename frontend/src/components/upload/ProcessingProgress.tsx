interface Props {
  progress: number;
  status: string;
}

export default function ProcessingProgress({
  progress,
  status,
}: Props) {
  const getMessage = () => {
    switch (status) {
      case "UPLOADED":
        return "Upload completed...";

      case "PROCESSING":
        return "Running OCR...";

      case "INDEXING":
        return "Indexing document...";

      case "OCR_COMPLETED":
        return "Processing completed.";

      default:
        return "Preparing...";
    }
  };

  return (
    <div className="mt-8 rounded-xl border bg-white p-6 shadow-sm">

      <h2 className="mb-4 text-xl font-semibold">
        Processing Document
      </h2>

      <div className="h-4 w-full overflow-hidden rounded-full bg-slate-200">

        <div
          className="h-full rounded-full bg-blue-600 transition-all duration-500"
          style={{ width: `${progress}%` }}
        />

      </div>

      <p className="mt-4 font-medium">
        {getMessage()}
      </p>

      <p className="mt-2 text-sm text-slate-500">
        {progress}%
      </p>

    </div>
  );
}