import {

    FileText,

    ScanText,

    Loader,

    Database,

} from "lucide-react";

import StatCard from "./StatCard";

import { DashboardStats } from "@/api/dashboard";

interface Props {

    stats: DashboardStats;

}

export default function StatsGrid({

    stats,

}: Props) {

    return (

        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

            <StatCard

                title="Documents"

                value={stats.total_documents}

                icon={FileText}

                color="bg-blue-600"

            />

            <StatCard

                title="OCR Completed"

                value={stats.ocr_completed}

                icon={ScanText}

                color="bg-green-600"

            />

            <StatCard

                title="Processing"

                value={stats.processing}

                icon={Loader}

                color="bg-orange-500"

            />

            <StatCard

                title="Indexed"

                value={stats.indexed}

                icon={Database}

                color="bg-purple-600"

            />

        </div>

    );

}