import { useState } from "react";
import { Document, Page } from "react-pdf";

import type { ViewerDocument } from "@/api/viewer";

interface Props {
  document: ViewerDocument;
}

export default function DocumentPreview({
  document,
}: Props) {

  const [numPages, setNumPages] = useState(0);

  const url = `http://127.0.0.1:8000${document.file_path}`;

  const extension = document.file_type.toLowerCase();

  if (
    extension === ".jpg" ||
    extension === ".jpeg" ||
    extension === ".png"
  ) {
    return (
      <img
        src={url}
        alt={document.original_filename}
        className="w-full rounded-lg border"
      />
    );
  }

  if (extension === ".pdf") {
    return (
      <div className="rounded-lg border p-4 bg-white">

        <Document
          file={url}
          onLoadSuccess={({ numPages }) =>
            setNumPages(numPages)
          }
        >
          {Array.from(
            new Array(numPages),
            (_, index) => (
              <Page
                key={index}
                pageNumber={index + 1}
                width={700}
                className="mb-6"
              />
            )
          )}
        </Document>

      </div>
    );
  }

  return (
    <div className="rounded-lg border p-8 text-center">
      Preview not available.
    </div>
  );
}