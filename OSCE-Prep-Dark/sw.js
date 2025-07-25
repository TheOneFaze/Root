const CACHE_NAME = 'osce-prep-cache-v1';
const urlsToCache = [
  // Core HTML file
  '/OSCE-Prep-Dark/OSCE%20Page/index.html', //

  // The new authentication check script
  '/OSCE-Prep-Dark/OSCE%20Page/auth-check.js', //

  // Your login page
  '/OSCE-Prep-Dark/OSCE%20Page/login.html', //

  // Images from the OSCE Page/ directory
  '/OSCE-Prep-Dark/OSCE%20Page/Icon.png', //
  '/OSCE-Prep-Dark/OSCE%20Page/OSCE%20SPARK.png', //
  '/OSCE-Prep-Dark/OSCE%20Page/OSCE%20SPARK%20-%20Copy.png', //

  // Your main page's apple-touch-icon (if you keep it in OSCE Page/)
  // Make sure this path is accurate if you rename/move it.
  '/OSCE-Prep-Dark/OSCE%20Page/apple-touch-icon.png', //

  // Add the new icons you'll create in the root /icons/ folder
  '/OSCE-Prep-Dark/icons/icon-192x192.png',
  '/OSCE-Prep-Dark/icons/icon-512x512.png',

  // All individual History Taking HTML files
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Abdominal%20Pain.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Anxiety.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Breast%20Lump.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Cardiovascular.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Chest%20Pain.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Cough.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Depression.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Dizziness%20History.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Dysphagia.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Dyspnoea.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Falls.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Female%20LUTS.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Headache.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Leg%20Swelling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Loss%20of%20Consciousness.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Male%20LUTS.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Ophthalmic.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Palpitations.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Respiratory.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Seizure.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Stroke-TIA.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Tiredness.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Unintentional%20Weight%20Loss.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/History%20Taking/Urological.html', //

  // Main category pages
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_community_stations.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_history_taking.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_post-procedure__stations.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_procedure_stations.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_surgery_stations.html', //

  // Community Stations
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_community_stations/alcohol_cessation_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_community_stations/bowel_cancer_screening_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_community_stations/community_blood_pressure_check.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_community_stations/dnacpr_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_community_stations/hypertension_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_community_stations/inhaler_technique_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_community_stations/peak_flow_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_community_stations/smoking_cessation_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_community_stations/weight_loss_counselling.html', //

  // Diagnosis Stations
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations/atrial_fibrillation_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations/bacterial_vaginosis_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations/chronic_kidney_disease_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations/explaining_a_diagnosis_of_asthma.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations/explaining_diagnosis_copd.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations/explaining_diagnosis_eczema.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations/explaining_diagnosis_fibroadenoma.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations/explaining_diagnosis_glaucoma.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations/explaining_diagnosis_type1_diabetes.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations/explaining_diagnosis_type2_diabetes.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_diagnosis_stations/hypertension_counselling.html', //

  // Medication Stations
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/ace_inhibitor_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/amitriptyline_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/anticoagulant_counselling_pharmacy.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/asthma_spacer_explanation.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/direct_oral_anticoagulant_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/gliclazide_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/gtn_spray_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/inhaler_counselling_01_pharmacy.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/inhaler_counselling_02_pharmacy.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/insulin_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/iron_supplementation_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/metformin_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/opioid_analgesia_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/ssri_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/statin_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_medication_stations/warfarin_counselling.html', //

  // Post-Procedure Stations
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_post-procedure__stations/post_stemi_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_post-procedure__stations/post_stroke_counselling.html', //

  // Procedure Stations
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_procedure_stations/ascitic_drain_explanation.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_procedure_stations/blood_transfusion_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_procedure_stations/bronchoscopy_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_procedure_stations/chest_drain_explanation.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_procedure_stations/colonoscopy_explanation.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_procedure_stations/echocardiogram_explanation.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_procedure_stations/endoscopy_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_procedure_stations/ercp_explanation.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_procedure_stations/haemodialysis_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_procedure_stations/tuberculosis_treatment_counselling.html', //

  // Surgery Stations
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_surgery_stations/appendicectomy_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_surgery_stations/cabg_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_surgery_stations/cholecystectomy_counselling.html', //
  '/OSCE-Prep-Dark/OSCE%20Page/Main%20Page/pretty_surgery_stations/gastrectomy_counselling.html', //

  // Other assets like images and potentially common CSS/JS if not inlined
  '/OSCE-Prep-Dark/OSCE%20Page/Icon.png', //
  '/OSCE-Prep-Dark/OSCE%20Page/OSCE%20SPARK.png', //
  '/OSCE-Prep-Dark/OSCE%20Page/OSCE%20SPARK%20-%20Copy.png', //
  '/OSCE-Prep-Dark/OSCE%20Page/apple-touch-icon.png', //
  '/OSCE-Prep-Dark/icons/icon-192x192.png', //
  '/OSCE-Prep-Dark/icons/icon-512x512.png', //
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Service Worker: Caching App Shell');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Cache hit - return response
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('Service Worker: Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
