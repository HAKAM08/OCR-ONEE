import { useState } from "react";
import { useNavigate } from "react-router-dom";

import DocumentsToolbar from "@/components/documents/DocumentsToolbar";
import DocumentsTable from "@/components/documents/DocumentsTable";

import { useDocuments } from "@/hooks/useDocuments";
import { useDeleteDocument } from "@/hooks/useDeleteDocument";

export default function Documents() {

    const navigate = useNavigate();

    const [search, setSearch] = useState("");

    const {

        data,

        isLoading,

        isError,

    } = useDocuments();

    const deleteMutation = useDeleteDocument();

    if (isLoading) {

        return <div>Loading...</div>;

    }

    if (isError || !data) {

        return <div>Error.</div>;

    }

    const filtered = data.filter((doc) =>

        doc.original_filename
            .toLowerCase()
            .includes(search.toLowerCase())

    );

    return (

        <div className="space-y-6">

            <div>

                <h1 className="text-3xl font-bold">

                    Documents

                </h1>

            </div>

            <DocumentsToolbar

                value={search}

                onChange={setSearch}

            />

            <DocumentsTable

                documents={filtered}

                onDelete={(id) =>

                    deleteMutation.mutate(id)

                }

                onView={(id) =>

                    navigate(`/viewer/${id}`)

                }

            />

        </div>

    );

}