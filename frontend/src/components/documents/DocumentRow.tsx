import {

    Eye,

    Trash2,

    FileText,

} from "lucide-react";
import DeleteDialog from "@/components/common/DeleteDialog";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";

import { Document } from "@/api/documents";

interface Props {

    document: Document;

    onDelete: (id: number) => void;

    onView: (id: number) => void;

}

export default function DocumentRow({

    document,

    onDelete,

    onView,

}: Props) {

    const getVariant = () => {

        switch (document.status) {

            case "OCR_COMPLETED":
                return "default";

            case "PROCESSING":
                return "secondary";

            default:
                return "outline";

        }

    };

    return (

        <tr className="border-b hover:bg-slate-50 transition">

            <td className="px-6 py-4">

<div className="flex items-center gap-4">

    {document.file_type === ".pdf" ? (

        <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-red-100">

            <FileText
                className="text-red-600"
                size={28}
            />

        </div>

    ) : (

        <img
            src={`http://127.0.0.1:8000/uploads/documents/${document.filename}`}
            alt={document.original_filename}
            className="h-14 w-14 rounded-lg border object-cover"
        />

    )}

    <div>

        <div className="font-medium">

            {document.original_filename}

        </div>

        <div className="text-sm text-slate-500">

            {document.file_type.toUpperCase()}

        </div>

    </div>

</div>

            </td>

            <td className="px-6 py-4">

                {document.file_type}

            </td>

            <td className="px-6 py-4">

                <Badge variant={getVariant()}>

                    {document.status}

                </Badge>

            </td>

            <td className="px-6 py-4">

                {new Date(
                    document.upload_date
                ).toLocaleString()}

            </td>

            <td className="px-6 py-4">

                <div className="flex gap-2">

                    <Button
                        size="icon"
                        variant="outline"
                        onClick={() => onView(document.id)}
                    >

                        <Eye size={18} />

                    </Button>

                    <DeleteDialog
    onConfirm={() => onDelete(document.id)}
>

    <Button
        size="icon"
        variant="destructive"
    >

        <Trash2 size={18} />

    </Button>

</DeleteDialog>

                </div>

            </td>

        </tr>

    );

}