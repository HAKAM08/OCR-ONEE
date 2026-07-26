import DocumentRow from "./DocumentRow";

import { Document } from "@/api/documents";

interface Props {
    documents: Document[];
    onDelete: (id: number) => void;
    onView: (id: number) => void;
}

export default function DocumentsTable({
    documents,
    onDelete,
    onView,
}: Props) {
    return (
        <div className="overflow-hidden rounded-xl border bg-white shadow-sm">
            <table className="w-full table-fixed">
                <thead className="bg-slate-100">
                    <tr>
                        <th className="w-[35%] px-6 py-4 text-left font-semibold">
                            Filename
                        </th>

                        <th className="w-[12%] px-6 py-4 text-left font-semibold">
                            Type
                        </th>

                        <th className="w-[18%] px-6 py-4 text-left font-semibold">
                            Status
                        </th>

                        <th className="w-[20%] px-6 py-4 text-left font-semibold">
                            Upload Date
                        </th>

                        <th className="w-[15%] px-6 py-4 text-center font-semibold">
                            Actions
                        </th>
                    </tr>
                </thead>

                <tbody>
                    {documents.length === 0 ? (
                        <tr>
                            <td
                                colSpan={5}
                                className="py-10 text-center text-slate-500"
                            >
                                No documents found.
                            </td>
                        </tr>
                    ) : (
                        documents.map((document) => (
                            <DocumentRow
                                key={document.id}
                                document={document}
                                onDelete={onDelete}
                                onView={onView}
                            />
                        ))
                    )}
                </tbody>
            </table>
        </div>
    );
}