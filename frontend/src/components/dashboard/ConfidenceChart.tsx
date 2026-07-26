import {
  ResponsiveContainer,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

interface Props {
  data: {
    name: string;
    value: number;
  }[];
}

export default function ConfidenceChart({
  data,
}: Props) {
  return (
    <div className="rounded-xl border bg-white p-6 shadow-sm">

      <h2 className="mb-6 text-lg font-semibold">
        OCR Confidence
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <AreaChart data={data}>

          <XAxis dataKey="name" />

          <YAxis />

          <Tooltip />

          <Area
            dataKey="value"
          />

        </AreaChart>

      </ResponsiveContainer>

    </div>
  );
}