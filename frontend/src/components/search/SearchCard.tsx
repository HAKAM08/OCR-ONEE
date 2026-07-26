import { Link } from "react-router-dom";
import { FileText, Globe, Target } from "lucide-react";
import type { SearchResult } from "@/api/search";

interface Props {
  result: SearchResult;
}

export default function SearchCard({
  result,
}: Props) {
  return (
    <div className="rounded-xl border bg-white p-6 shadow-sm">

      <div className="flex items-start justify-between">

        <div>

          <h2 className="text-lg font-semibold">
            {result.filename}
          </h2>

          <div className="mt-2 flex gap-3 text-sm text-slate-500">

            <span>
              🌍 {result.language}
            </span>

            <span>
              🎯 {result.confidence.toFixed(1)}%
            </span>

          </div>

        </div>

        <Link
          to={`/viewer/${result.id}`}
          className="rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
        >
          Open
        </Link>

      </div>

      <p
  className="mt-4 leading-7 text-slate-700"
  dangerouslySetInnerHTML={{
    __html: result.snippet.replaceAll(
      "<em>",
      '<mark class="rounded bg-yellow-200 px-1">'
    ).replaceAll(
      "</em>",
      "</mark>"
    ),
  }}
/>

    </div>
  );
}