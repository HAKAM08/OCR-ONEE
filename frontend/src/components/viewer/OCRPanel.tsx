import { Card } from "@/components/ui/card";

interface Props {

    text: string;

}

export default function OCRPanel({

    text,

}: Props) {

    return (

        <Card className="p-6 h-full">

            <h2 className="mb-4 text-xl font-semibold">

                OCR Text

            </h2>

            <pre className="whitespace-pre-wrap text-sm">

                {text}

            </pre>

        </Card>

    );

}