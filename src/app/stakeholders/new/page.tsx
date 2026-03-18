import StakeholderForm from '@/components/StakeholderForm';

export default function NewStakeholderPage() {
  return (
    <div className="space-y-5 max-w-2xl">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">Add Stakeholder</h2>
        <p className="text-sm text-slate-500 mt-0.5">Register a new stakeholder in the system</p>
      </div>
      <StakeholderForm />
    </div>
  );
}
