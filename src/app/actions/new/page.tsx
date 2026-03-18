import ActionForm from '@/components/ActionForm';
import { getStakeholders } from '@/lib/store';

export const dynamic = 'force-dynamic';

export default function NewActionPage() {
  const stakeholders = getStakeholders();
  return (
    <div className="space-y-5 max-w-2xl">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">New Action</h2>
        <p className="text-sm text-slate-500 mt-0.5">Create a tactical action or engagement task</p>
      </div>
      <ActionForm stakeholders={stakeholders} />
    </div>
  );
}
