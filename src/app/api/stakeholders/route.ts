import { NextRequest, NextResponse } from 'next/server';
import { getStakeholders, createStakeholder } from '@/lib/store';

export async function GET() {
  const stakeholders = getStakeholders();
  return NextResponse.json(stakeholders);
}

export async function POST(req: NextRequest) {
  const body = await req.json();
  const { name, organization, role, email, phone, category, influence, interest, notes, tags } = body;

  if (!name || !organization || !role || !email || !category || !influence || !interest) {
    return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
  }

  const stakeholder = createStakeholder({
    name, organization, role, email,
    phone: phone || '',
    category, influence, interest,
    notes: notes || '',
    tags: tags || [],
  });

  return NextResponse.json(stakeholder, { status: 201 });
}
