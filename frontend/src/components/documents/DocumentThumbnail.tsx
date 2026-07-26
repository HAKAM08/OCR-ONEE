interface Props {
  fileType: string;
  thumbnail: string;
}

export default function DocumentThumbnail({
  fileType,
  thumbnail,
}: Props) {

  const url =
    `http://127.0.0.1:8000${thumbnail}`;

  if (
    fileType === ".jpg" ||
    fileType === ".jpeg" ||
    fileType === ".png"
  ) {

    return (

      <img
        src={url}
        alt=""
        className="h-28 w-40 rounded-lg object-cover border"
      />

    );

  }

  if (fileType === ".pdf") {

    return (

      <div className="flex h-28 w-40 items-center justify-center rounded-lg border bg-red-50">

        <span className="text-4xl">
          📄
        </span>

      </div>

    );

  }

  return (

    <div className="flex h-28 w-40 items-center justify-center rounded-lg border">

      File

    </div>

  );

}