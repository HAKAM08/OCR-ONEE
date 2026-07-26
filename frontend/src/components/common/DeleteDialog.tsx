import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";

interface Props {
  onConfirm: () => void;
  children: React.ReactNode;
}

export default function DeleteDialog({
  children,
  onConfirm,
}: Props) {
  return (
    <AlertDialog>

      <AlertDialogTrigger asChild>
        {children}
      </AlertDialogTrigger>

      <AlertDialogContent>

        <AlertDialogHeader>

          <AlertDialogTitle>
            Delete document?
          </AlertDialogTitle>

          <AlertDialogDescription>
            This action cannot be undone.
          </AlertDialogDescription>

        </AlertDialogHeader>

        <AlertDialogFooter>

          <AlertDialogCancel>
            Cancel
          </AlertDialogCancel>

          <AlertDialogAction
            onClick={onConfirm}
          >
            Delete
          </AlertDialogAction>

        </AlertDialogFooter>

      </AlertDialogContent>

    </AlertDialog>
  );
}