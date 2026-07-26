interface Props {

  value: string;

  onChange: (value: string) => void;

}

export default function SearchInput({

  value,

  onChange,

}: Props) {

  return (

    <input

      className="w-full rounded-xl border bg-white p-4 text-lg"

      placeholder="Search documents..."

      value={value}

      onChange={(e) => onChange(e.target.value)}

    />

  );

}