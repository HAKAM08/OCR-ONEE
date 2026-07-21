import { Card } from "@/components/ui/card";

import { ViewerDocument } from "@/api/viewer";

interface Props {

    document: ViewerDocument;

}

export default function MetadataPanel({

    document,

}: Props) {

    return (

        <Card className="p-6">

            <h2 className="mb-4 text-xl font-semibold">

                Metadata

            </h2>

            <div className="space-y-3">

                <p>

                    <strong>Language:</strong>{" "}

                    {document.language}

                </p>

                <p>

                    <strong>Confidence:</strong>{" "}

                    {document.confidence.toFixed(2)} %

                </p>

                <p>

                    <strong>Processing Time:</strong>{" "}

                    {document.processing_time} s

                </p>

                <p>

                    <strong>Status:</strong>{" "}

                    {document.status}

                </p>

            </div>

        </Card>

    );

}