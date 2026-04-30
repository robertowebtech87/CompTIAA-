#!/bin/bash
# Run from comptia_quiz/ folder:
# bash reorganize_seeds.sh

echo "Creating subfolders..."
mkdir -p seeds/core1
mkdir -p seeds/core2
mkdir -p seeds/intro
mkdir -p seeds/migrations

echo "Moving Core 1 seeds..."
for f in seed_complete seed_new_questions seed_top50 seed_multi_select \
          seed_exam_practice seed_exam_practice2 seed_troubleshooting_core1 \
          seed_laptop_hardware seed_study_guide_q16_37 \
          seed_mobile_connectivity seed_mobile_optimization \
          seed_mobile_extra seed_mobile_advanced seed_missing_objectives \
          seed_networking_and_scenarios seed_networking_objectives \
          seed_networking_advanced seed_networking_messer \
          seed_ports_protocols seed_ports_extended seed_subnetting; do
    [ -f "seeds/$f.py" ] && mv "seeds/$f.py" "seeds/core1/" && echo "  moved $f.py"
done

echo "Moving Core 2 seeds..."
for f in seed_core2_batch1 seed_core2_batch2 seed_core2_batch3 \
          seed_core2_batch4 seed_core2_batch5 seed_core2_batch6 \
          seed_core2_batch7 seed_core2_batch8 seed_core2_final; do
    [ -f "seeds/$f.py" ] && mv "seeds/$f.py" "seeds/core2/" && echo "  moved $f.py"
done

echo "Moving IT Fundamentals..."
[ -f "seeds/seed_it_fundamentals.py" ] && mv seeds/seed_it_fundamentals.py seeds/intro/ && echo "  moved seed_it_fundamentals.py"

echo "Moving migrations..."
for f in migrate_add_exam migrate_multi_select migrate_spaced_repetition migrate_intro_exam; do
    [ -f "seeds/$f.py" ] && mv "seeds/$f.py" "seeds/migrations/" && echo "  moved $f.py"
done

echo ""
echo "Adding Python path fix to all seed files..."
for f in seeds/core1/*.py seeds/core2/*.py seeds/intro/*.py seeds/migrations/*.py; do
    if [ -f "$f" ] && ! grep -q "sys.path.insert" "$f"; then
        tmp=$(mktemp)
        echo 'import sys, os' > "$tmp"
        echo 'sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))' >> "$tmp"
        echo '' >> "$tmp"
        cat "$f" >> "$tmp"
        mv "$tmp" "$f"
        echo "  fixed: $f"
    fi
done

echo ""
echo "Done! Structure:"
echo "seeds/core1/  -> $(ls seeds/core1/ | wc -l | tr -d ' ') files"
echo "seeds/core2/  -> $(ls seeds/core2/ | wc -l | tr -d ' ') files"
echo "seeds/intro/  -> $(ls seeds/intro/ | wc -l | tr -d ' ') files"
echo "seeds/migrations/ -> $(ls seeds/migrations/ | wc -l | tr -d ' ') files"
echo ""
echo "Test with: python3 seeds/intro/seed_it_fundamentals.py"
