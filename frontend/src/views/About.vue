<template>
  <div>

    <profile/>
    <stack/>
    <statistics/>
    
  </div>
</template>

<script>
import Statistics from '../components/aboutdata/Statistics'
import Profile from '../components/aboutdata/Profile'
import Stack from '../components/aboutdata/Stack'
export default {
  name: 'About',
  components: {
    Statistics,
    Profile,
    Stack
  }

}
</script>