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

            <table className="w-full">

                <thead className="bg-slate-100">

                    <tr>

                        <th className="px-6 py-4 text-left">

                            Filename

                        </th>

                        <th className="px-6 py-4 text-left">

                            Type

                        </th>

                        <th className="px-6 py-4 text-left">

                            Status

                        </th>

                        <th className="px-6 py-4 text-left">

                            Upload Date

                        </th>

                        <th className="px-6 py-4 text-left">

                            Actions

                        </th>

                    </tr>

                </thead>

                <tbody>

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

                </tbody>

            </table>

        </div>

    );

}