import StatsGrid from "@/components/dashboard/StatsGrid";
import RecentDocuments from "@/components/dashboard/RecentDocuments";
import SystemStatus from "@/components/dashboard/SystemStatus";
import StatsSkeleton from "@/components/dashboard/StatsSkeleton";

import StatisticsChart from "@/components/dashboard/StatisticsChart";
import LanguagesChart from "@/components/dashboard/LanguagesChart";
import ConfidenceChart from "@/components/dashboard/ConfidenceChart";

import { useDashboard } from "@/hooks/useDashboard";

export default function Dashboard() {

    const {

        data,

        isLoading,

        isError,

    } = useDashboard();

    if (isLoading) {

        return <StatsSkeleton />;

    }

    if (isError || !data) {

        return (

            <div className="text-red-600">

                Unable to load dashboard.

            </div>

        );

    }

    return (

        <div className="space-y-8">

            <div>

                <h1 className="text-3xl font-bold">

                    Dashboard

                </h1>

                <p className="mt-2 text-slate-500">

                    Overview of your OCR platform

                </p>

            </div>

            <StatsGrid
                stats={data}
            />

            <div className="grid gap-6 lg:grid-cols-2">

                <StatisticsChart

                    data={[

                        {
                            name: "Uploaded",
                            value: data.total_documents,
                        },

                        {
                            name: "Completed",
                            value: data.completed_documents,
                        },

                        {
                            name: "Processing",
                            value: data.processing_documents,
                        },

                    ]}

                />

                <LanguagesChart
    data={data.detected_languages.map((item) => ({
        name: item.language,
        value: item.count,
    }))}
/>

            </div>

            <ConfidenceChart

                data={[

                    {

                        name: "OCR",

                        value: data.average_confidence,

                    }

                ]}

            />

            <div className="grid gap-8 xl:grid-cols-3">

                <div className="xl:col-span-2">

                    <RecentDocuments
                        stats={data}
                    />

                </div>

                <SystemStatus />

            </div>

        </div>

    );

}