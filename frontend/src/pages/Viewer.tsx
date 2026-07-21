import { useParams } from "react-router-dom";

import { useViewer } from "@/hooks/useViewer";

import MetadataPanel from "@/components/viewer/MetadataPanel";
import OCRPanel from "@/components/viewer/OCRPanel";
import DocumentPreview from "@/components/viewer/DocumentPreview";

export default function Viewer() {

    const { id } = useParams();

    const {

        data,

        isLoading,

        isError,

    } = useViewer(Number(id));

    if (isLoading) {

        return (

            <div className="p-10">

                Loading document...

            </div>

        );

    }

    if (isError || !data) {

        return (

            <div className="p-10 text-red-500">

                Unable to load document.

            </div>

        );

    }

    return (

        <div className="space-y-6">

            <div>

                <h1 className="text-3xl font-bold">

                    {data.original_filename}

                </h1>

                <p className="text-slate-500">

                    Document Viewer

                </p>

            </div>

            <div className="grid gap-6 lg:grid-cols-3">

                <div className="space-y-6 lg:col-span-2">

    <DocumentPreview

        document={data}

    />

    <OCRPanel

        text={data.text}

    />

</div>

                <MetadataPanel

                    document={data}

                />

            </div>

        </div>

    );

}