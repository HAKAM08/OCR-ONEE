import {

    Eye,

    FileText,

    Calendar,

} from "lucide-react";

import {

    Card,

} from "@/components/ui/card";

import {

    Badge,

} from "@/components/ui/badge";

import {

    Button,

} from "@/components/ui/button";

import {

    DashboardStats,

} from "@/api/dashboard";
import { useNavigate } from "react-router-dom";
interface Props {

    stats: DashboardStats;

}

export default function RecentDocuments({

    stats,

}: Props) {

    const navigate = useNavigate();

    return (

        <Card className="mt-8">

            <div className="border-b p-6">

                <h2 className="text-xl font-semibold">

                    Recent Documents

                </h2>

                <p className="text-sm text-slate-500">

                    Latest uploaded files

                </p>

            </div>

            <div className="divide-y">

                {stats.recent_documents.map((document) => (

                    <div
                        key={document.id}
                        className="flex items-center justify-between p-5 hover:bg-slate-50 transition"
                    >

                        <div className="flex items-center gap-4">

                            <div className="rounded-lg bg-blue-100 p-3">

                                <FileText
                                    className="text-blue-600"
                                    size={22}
                                />

                            </div>

                            <div>

                                <p className="font-medium">

                                    {document.filename}

                                </p>

                                <div className="mt-1 flex items-center gap-2 text-sm text-slate-500">

                                    <Calendar size={14} />

                                    {new Date(
                                        document.upload_date
                                    ).toLocaleString()}

                                </div>

                            </div>

                        </div>

                        <div className="flex items-center gap-4">

                            <Badge
                                variant={
                                    document.status === "OCR_COMPLETED"
                                        ? "default"
                                        : document.status === "PROCESSING"
                                        ? "secondary"
                                        : "destructive"
                                }
                            >

                                {document.status}

                            </Badge>
                           <Button
    variant="outline"
    size="icon"
    onClick={() =>
        navigate(`/viewer/${document.id}`)
    }
>

    <Eye size={18} />

</Button>

                        </div>

                    </div>

                ))}

            </div>

        </Card>

    );

}