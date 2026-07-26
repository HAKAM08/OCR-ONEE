import { useState } from "react";

import SearchInput from "@/components/search/SearchInput";
import SearchCard from "@/components/search/SearchCard";

import { useSearch } from "@/hooks/useSearch";
import { useDebounce } from "@/hooks/useDebounce";

export default function Search() {

  const [query, setQuery] = useState("");

  const debouncedQuery = useDebounce(query, 300);

  const {
    data,
    isLoading,
  } = useSearch(debouncedQuery);

  return (

    <div className="mx-auto max-w-6xl space-y-8">

      <div>

        <h1 className="text-3xl font-bold">

          Search Documents

        </h1>

        <p className="mt-2 text-slate-500">

          Search inside every OCR document using Elasticsearch.

        </p>

      </div>

      <SearchInput

        value={query}

        onChange={setQuery}

      />

      {query.length < 2 && (

        <div className="rounded-xl border bg-white p-12 text-center text-slate-500">

          Start typing to search your documents.

        </div>

      )}

      {isLoading && (

        <div className="rounded-xl border bg-white p-12 text-center">

          Searching...

        </div>

      )}

      {query.length >= 2 &&
        !isLoading &&
        data?.length === 0 && (

        <div className="rounded-xl border bg-white p-12 text-center">

          No matching documents found.

        </div>

      )}

      <div className="space-y-6">

        {data?.map((result) => (

          <SearchCard

            key={result.id}

            result={result}

          />

        ))}

      </div>

    </div>

  );

}