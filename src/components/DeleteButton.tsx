'use client';

import { useRouter } from 'next/navigation';

export default function DeleteButton({ id, type }: { id: string; type: 'stakeholders' | 'relations' | 'actions' }) {
  const router = useRouter();

  async function handleDelete() {
    if (!confirm('Are you sure you want to delete this item?')) return;
    await fetch(`/api/${type}/${id}`, { method: 'DELETE' });
    router.refresh();
  }

  return (
    <button onClick={handleDelete} className="text-xs text-red-500 hover:underline">
      Delete
    </button>
  );
}
